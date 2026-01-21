# ⏰ Reloj Despertador en Python

Proyecto educativo en Python que implementa un reloj despertador ejecutado desde la línea de comandos (CLI).

---

## 🧠 Idea del proyecto

Este no es un reloj despertador tradicional.

- El usuario configura una alarma para una hora específica
- La aplicación lee un archivo de texto con URLs de YouTube
- Al activarse la alarma:
  - Se selecciona una URL aleatoria
  - Se reproduce automáticamente en el navegador

---

## 🛠️ Tecnologías

- **Python 3.11+**

---

## 📂 Estructura del proyecto

```
reloj_despertador/
│
├── src/                 
│   └── main.py
├── data/                 
│   └── youtube_links.txt
│
├── .gitignore
├── README.md
```

---

## ⚙️ Instalación

#### 1. Asegúrate de tener **Python 3.11 o superior** instalado.

1. 1  (Opcional) Crear un entorno virtual con conda

   ```
    conda create -n reloj_despertador_env python=3.11
    conda activate reloj_despertador_env
   ```

#### 2. Clona el repositorio:

   ```
   git clone https://github.com/RoniPG/reloj_despertador.git
   ```

#### 3. Accede al directorio del proyecto:

   ```
    cd reloj_despertador
   ```

---

## :rocket: Uso

Desde la raíz del proyecto, ejecuta:
   ```
    python src/main.py
   ```

---