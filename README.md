<div align="center">

  <br>

  <h1><img src="https://img.icons8.com/ios/256/FFFFFF/shield.png" width="35" valign="middle">&nbsp; REGLAS DE DETECCIÓN SIEM</h1>

  <img src="https://img.shields.io/badge/Estado-Activo-000000?style=for-the-badge&logo=activity&logoColor=white">
  <img src="https://img.shields.io/badge/Reglas-25+-000000?style=for-the-badge&logo=files&logoColor=white">
  <img src="https://img.shields.io/badge/Licencia-MIT-000000?style=for-the-badge&logo=opensourceinitiative&logoColor=white">
  <img src="https://img.shields.io/badge/Plataforma-Splunk_|_Elastic_|_QRadar-000000?style=for-the-badge&logo=server&logoColor=white">

  <br><br>

  > **Una colección profesional de reglas de detección de alta fidelidad para entornos SOC modernos.**<br>
  > *Mantenido por [Ph0e-Nyx](https://github.com/Ph0e-Nyx)*

  <br>

  <a href="#reglas-de-detección"><img src="https://img.shields.io/badge/Explorar_Reglas-000000?style=for-the-badge&logo=search&logoColor=white"></a>
  <a href="#implementación"><img src="https://img.shields.io/badge/Implementación-000000?style=for-the-badge&logo=geeksforgeeks&logoColor=white"></a>
  <a href="https://github.com/Ph0e-Nyx/siem-detection-rules/pulls"><img src="https://img.shields.io/badge/Contribuir-000000?style=for-the-badge&logo=github&logoColor=white"></a>

</div>

<br><br>

<!-- SEPARADOR: RESUMEN -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=ffffff&text=RESUMEN&fontColor=000000&height=40&fontSize=22" width="100%"/>
</div>
<br>

<div align="justify">
  Este repositorio aloja una exhaustiva biblioteca de reglas de detección SIEM personalizadas, diseñadas para identificar amenazas avanzadas a lo largo de la cadena de ataque (<i>kill chain</i>). Cada regla está meticulosamente elaborada, probada y mapeada al framework <b>MITRE ATT&CK</b>.
</div>
<br>

### <img src="https://img.icons8.com/ios/256/FFFFFF/star.png" width="22" valign="middle"> Características Principales

* <img src="https://img.icons8.com/ios/256/FFFFFF/synchronize.png" width="18" valign="middle"> **Soporte Multiplataforma**: Reglas nativas para **Splunk** (SPL), **Elastic** (EQL/KQL) y **QRadar** (AQL), derivadas de una base universal en **Sigma**.
* <img src="https://img.icons8.com/ios/256/FFFFFF/grid.png" width="18" valign="middle"> **Integración con MITRE ATT&CK**: Mapeo completo a Tácticas, Técnicas y Procedimientos (TTPs).
* <img src="https://img.icons8.com/ios/256/FFFFFF/test-tube.png" width="18" valign="middle"> **Lógica Validada**: Reglas probadas contra simulaciones de ataques del mundo real (Atomic Red Team).
* <img src="https://img.icons8.com/ios/256/FFFFFF/ok.png" width="18" valign="middle"> **Bajos Falsos Positivos**: Ajustadas para minimizar el ruido en entornos de producción reales.
* <img src="https://img.icons8.com/ios/256/FFFFFF/document.png" width="18" valign="middle"> **Documentación Detallada**: Cada regla incluye contexto, puntos ciegos y guías de respuesta.

<br><br>

<!-- SEPARADOR: REGLAS DE DETECCION -->
<a name="reglas-de-detección"></a>
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=ffffff&text=REGLAS%20DE%20DETECCIÓN&fontColor=000000&height=40&fontSize=22" width="100%"/>
</div>
<br>

Las reglas están organizadas por **Tácticas de MITRE ATT&CK**:

| Táctica | Descripción | Cantidad |
| :--- | :--- | :---: |
| **[Acceso Inicial](rules/sigma/initial_access)** | Phishing, Cuentas Válidas, Explotación de Aplicaciones Públicas | 3 |
| **[Ejecución](rules/sigma/execution)** | PowerShell, LOLBins, Tareas Programadas | 5 |
| **[Persistencia](rules/sigma/persistence)** | Claves de Registro (Run), Servicios, Manipulación de Cuentas | 4 |
| **[Escalada de Privilegios](rules/sigma/privilege_escalation)** | Manipulación de Tokens, Evasión de UAC | 3 |
| **[Evasión de Defensas](rules/sigma/defense_evasion)** | Deterioro de Defensas, Eliminación de Indicadores, Enmascaramiento | 4 |
| **[Movimiento Lateral](rules/sigma/lateral_movement)** | RDP, Recursos Compartidos SMB/Admin, Pass the Hash | 3 |
| **[Comando y Control](rules/sigma/command_and_control)** | Protocolos Web, Tunelización DNS, Puertos No Estándar | 3 |
| **[Exfiltración](rules/sigma/exfiltration)** | Exfiltración sobre C2, Datos Preparados | 2 |

> [!TIP]
> Utiliza el **[Navegador de Reglas](docs/rules/README.md)** para buscar reglas concretas por origen de datos o ID de técnica.

<br><br>

<!-- SEPARADOR: IMPLEMENTACION -->
<a name="implementación"></a>
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&color=ffffff&text=IMPLEMENTACIÓN&fontColor=000000&height=40&fontSize=22" width="100%"/>
</div>
<br>

### <img src="https://img.icons8.com/ios/256/FFFFFF/checklist.png" width="22" valign="middle"> Requisitos Previos

* **Python 3.8+** (para las herramientas de validación)
* **Sigma CLI** (opcional, para conversiones personalizadas)

### <img src="https://img.icons8.com/ios/256/FFFFFF/rocket.png" width="22" valign="middle"> Inicio Rápido

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Ph0e-Nyx/siem-detection-rules.git
   cd siem-detection-rules
