@echo off
echo ========================================
echo    SUBIENDO CAMBIOS A GITHUB
echo ========================================
echo.

:: Cambiar a tu carpeta del proyecto
cd /d "C:\Users\kevin\OneDrive\Desktop\EMPRENDIMIENTO\MI PAGINA WEB"

:: Mostrar cambios pendientes
echo [1/4] VERIFICANDO CAMBIOS...
git status

:: Añadir todos los archivos
echo.
echo [2/4] AÑADIENDO ARCHIVOS...
git add .

:: Hacer commit con fecha y hora
echo.
echo [3/4] CREANDO COMMIT...
git commit -m "Update: %date% a las %time%"

:: Subir a GitHub
echo.
echo [4/4] SUBIENDO A GITHUB...
git push Origin main

:: Resultado final
echo.
echo ========================================
echo    ✓ CAMBIOS SUBIDOS EXITOSAMENTE
echo ========================================
echo.
timeout /t 5