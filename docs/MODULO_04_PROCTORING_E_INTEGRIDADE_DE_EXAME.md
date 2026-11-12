# Módulo 04 — Motor de Proctoring Simulado (Supervisão de Exame e Hardware Mocks)

Para emitir uma certificação técnica com valor real, o **Sistema de Educação e Certificação** inclui um subsistema de **Proctoring Automatizado** (`src/proctoring.py`) que monitora a integridade da avaliação prática sem depender de drivers proprietários ou hardware físico obrigatório durante os testes, utilizando **Injeção de Dependência e Mocks de Hardware**.

---

## 1. Arquitetura de Telemetria por Sensores Simulados (*Hardware Mocks*)

O motor de supervisão desacopla a leitura de hardware através de sensores simuláveis:
1. **Sensor de Webcam (`SensorWebcamMock`):** Reporta a quantidade de rostos detectados no quadro (`rostos_detectados`), direção do olhar (`olhar_na_tela`) e objetos proibidos (`celular_detectado`).
2. **Sensor de Áudio (`SensorAudioMock`):** Reporta o nível de pressão sonora em decibéis (`nivel_db`) e detecção de voz humana secundária (`fala_humana_detectada`).
3. **Sensor de Ambiente/Janela (`SensorJanelaMock`):** Monitora se a janela do exame está em primeiro plano (`foco_ativo`), quantos monitores estão conectados (`quantidade_monitores`) e eventos suspeitos de área de transferência (`tentativa_colar_externo`).

---

## 2. Regras "Carrasco" de Infração e Pontuação de Penalidade

Cada evento anômalo capturado durante a sessão de exame gera um registro imutável (`RegistroInfracao`) com gravidade e pontuação de risco:

| Código da Infração | Condição Detectada pelo Sensor | Gravidade | Pontos de Penalidade |
|---|---|---|---:|
| `AUSENCIA_ROSTO` | `rostos_detectados == 0` | Média | `35` |
| `MULTIPLOS_ROSTOS` | `rostos_detectados > 1` | Crítica | `60` |
| `CELULAR_DETECTADO` | `celular_detectado == True` | Eliminatória | `100` |
| `DESVIO_OLHAR` | `olhar_na_tela == False` | Leve | `20` |
| `AUDIO_SUSPEITO` | `nivel_db > 65.0` ou `fala_humana_detectada == True` | Média | `40` |
| `PERDA_FOCO_JANELA` | `foco_ativo == False` (ex.: `Alt+Tab`) | Alta | `50` |
| `MULTIPLOS_MONITORES` | `quantidade_monitores > 1` | Alta | `50` |
| `COLA_EXTERNA` | `tentativa_colar_externo == True` | Crítica | `70` |

### Limiares da Máquina de Estados da Sessão (`SessaoProctoring`)
- **0 pontos:** Status `INTEGRO` (Elegível para certificação).
- **1 a 99 pontos:** Status `ADVERTIDO` (Ainda elegível, porém com advertências registradas em ata).
- **$\ge 100$ pontos ou $\ge 3$ infrações acumuladas:** Status `ELIMINADO_POR_FRAUDE` (**Reprovação imediata e bloqueio irreversível de emissão do certificado SHA-256**).
