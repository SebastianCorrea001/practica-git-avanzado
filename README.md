# 🎲 Juego de Adivina el Número — Práctica de Git Avanzado

Proyecto simple de un juego de adivinar un número, usado
para practicar comandos avanzados de Git.

## ⚙️ Funcionalidades

- Genera un número aleatorio entre 1 y 100
- El usuario intenta adivinarlo
- Muestra pistas de "muy alto" o "muy bajo"
- Cuenta la cantidad de intentos usados
- Límite máximo de 10 intentos

## 📝 Cómo ejecutar
- python juego.py


---

## 📚 Teoría — Comandos que vas a usar

### git commit --amend

Modifica el ÚLTIMO commit que hiciste (cambia su mensaje y/o
agrega archivos que olvidaste). No crea un commit nuevo, corrige
el anterior.

### git commit --amend -m "nuevo mensaje"


### git reset

Deshace commits. `HEAD~1` significa "un commit atrás del actual"
(`HEAD~2` serían dos atrás, etc.)

Tiene 3 tipos:

- `--soft`: deshace el commit, pero tus cambios siguen listos
para volver a commitear
- `--mixed` (el que se usa si no escribes nada): deshace el
commit y el "add", los cambios quedan en tus archivos sin preparar
- `--hard`: borra TODO, incluso los cambios en tus archivos
(¡cuidado, esto no se puede deshacer!)


### git reset --soft HEAD~1


---

## 🔍 Investigación adicional

El comando `git reflog` muestra el historial completo de todos
los movimientos de HEAD (commits, resets, amends, etc.), incluso
los que ya no aparecen en `git log --oneline`. Esto es útil
porque permite recuperar commits "perdidos" (por ejemplo, tras
un reset o un amend), ya que Git no los borra de inmediato,
solo deja de mostrarlos en el historial normal.

## ✅ Entrega

Link de repositorio (fork): https://github.com/SebastianCorrea001/practica-git-avanzado

Pantallazo de `git log --oneline`: (agregar aquí la imagen)

