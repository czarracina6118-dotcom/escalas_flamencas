# Escalas Flamencas para Android

El APK incluye la página original, sus iconos y 16 muestras de guitarra española.
Escalas, acordes, cadencias, metrónomo y compás funcionan sin conexión. Al salir
se detienen los temporizadores y el audio. No solicita acceso al micrófono.

## Generar y descargar

En GitHub, abrir Actions → Generar APK de escalas → una ejecución verde →
Artifacts → Escalas-Flamencas-APK. Descomprimir el ZIP e instalar
`Escalas-Flamencas-1.0-prueba.apk`. El icono aparece como «Escalas APK».
Requiere Android 8 o posterior y un Android System WebView actualizado.

Para compilar localmente, con JDK 17, Gradle 8.11.1 y Android SDK 35:

```sh
python3 android/prepare_samples.py
cd android
gradle assembleDebug lintDebug
```

El script descarga las muestras FreePats desde una revisión fija y comprueba
SHA-256 antes de incluirlas. Fuente y licencia CC0:
https://github.com/freepats/spanish-classical-guitar
La licencia completa también se incluye dentro del APK junto a las muestras.

Validación en dispositivo: abrir sin conexión; cargar las muestras; escuchar
notas, escala ascendente/descendente, acordes y compás; comprobar legibilidad
en móvil/tablet, detener reproducción y comprobar silencio al salir.

La firma es de prueba: otra compilación puede requerir desinstalar la anterior.
Una distribución definitiva requiere una clave de firma privada permanente.
