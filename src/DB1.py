# Backend (FastAPI + SQL Server)
from fastapi import FastAPI, HTTPException, Depends, status, UploadFile, File, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, ForeignKey, LargeBinary
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.sql import select, insert, update, delete, and_, or_
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict, Union, Any, Literal
from datetime import datetime, date, timedelta
import pyodbc

# Frontend (Flet)
import flet as ft
from flet import *
import requests
import json
import datetime
from datetime import date
from datetime import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=tcp:10.83.10.154,1433;"
        "DATABASE=GAAWDB;"
        "Trusted_Connection=yes;"
    )


class VotoRequest(BaseModel):
    id_voto: Optional[int] = None
    votado: bool
    nome_jogo: str 
    usuario: Optional[str] = None
    venceu: Optional[bool] = None   
    
class JogoRequest(BaseModel):
    id_jogo: Optional[int] = None
    nome_jogo: str
    genero: str
    data_lancamento: int
    produtor: Optional[str] = None
    descricao: Optional[str] = None
    imagem: Optional[str] = None
    metacritic_score: Optional[float] = None

## Rota para listar jogos disponiveis para votação
@app.get("/jogos")
def listar_jogos():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM JOGOS")
        
        colunas = [column[0] for column in cursor.description]
        jogos = [dict(zip(colunas, row)) for row in cursor.fetchall()]
        
        conn.close()
        return {"jogos_disponiveis": jogos}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# Rota para registrar um novo jogo
@app.post("/novo_jogo")
def novo_jogo(jogo: JogoRequest):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO JOGOS (title, genre, releaseDate) VALUES (?, ?, ?)",
            (jogo.nome_jogo, jogo.genero, jogo.data_lancamento)
        )
        conn.commit()
        conn.close()
        return {"mensagem": "Jogo registrado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#Rota para atualizar um jogo existente
@app.put("/atualizar_jogo/{id_jogo}")
def atualizar_jogo(id_jogo: int, jogo: JogoRequest):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE JOGOS SET title = ?, genre = ?, releaseDate = ? WHERE id = ?",
            (jogo.nome_jogo, jogo.genero, jogo.data_lancamento, id_jogo)
        )
        conn.commit()
        conn.close()
        return {"mensagem": "Jogo atualizado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#Rota para Votar em um jogo
@app.post("/votar")
def votar(voto: VotoRequest):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO VOTOS (voted, username, gametitle) VALUES (?, ?, ?)",
            (1 if voto.votado else 0, voto.usuario, voto.nome_jogo)  # Converte bool para 1/0
        )
        conn.commit()
        conn.close()
        return {"mensagem": "Voto registrado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))