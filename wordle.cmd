@echo off
mode con: cols=45 lines=16
color>nul
python wordle.py && exit
py wordle.py
