<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# MCP infratuzilma toʻplami

![Namoyish](screenshots/demo.svg)
[![CI](https://github.com/uMax-Cyber/MCPForge/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/MCPForge/actions/workflows/ci.yml)

Model Context Protocol (MCP) serverlarini production infratuzilmada — fayrvol, tarmoq kontrolleri, gipervizorda — xavfsiz ishlatish uchun arxitektura naqshlari va himoya mexanizmlari. Hammasi haqiqiy joylashtirish tajribasidan yigʻilgan: 6 ta MCP server, 312 ta tool, guardrail qoʻyilgan holda toʻliq kirish.

## Muammo

MCP serverlar AI agentga production infratuzilmaga toʻgʻridan-toʻgʻri kirish beradi. Aniq tartib boʻlmasa, kuchsiz LLM parametrlarni oʻylab topadi, har xil manbadan olgan maʼlumotni aralashtirib yuboradi, xatoni maʼlumotdan ajrata olmaydi. Shu muammolarga qarshi ishlaydigan naqshlar — ana shu toʻplamda.

## Asosiy naqshlar

### 1. Routlangan tool naqshi (katta kataloglar uchun)
Serverda 200 dan ortiq tool boʻlsa, LLM ga hammasini koʻrsatish shart emas. Oʻrniga:
```
route_tools(query="list VMs") → kerakli toollarning nomini qaytaradi
call_routed_tool(name="list_vms", arguments={...})
```
Natijada 200 ta tool oʻrniga faqat 3 tasi koʻrinadi — kontekst oynasi tejaladi.

### 2. Xavfsizlik darajalari (avtonomiya darajalari)
```
🟢 YASHIL — oʻqish/roʻyxat/status: bemalol bajaraveradi
🟡 SARIQ — oʻchirish/rollback/resizing: avval foydalanuvchidan tasdiq oling
🔴 QIZIL — muhim infratuzilma (agentning oʻz hosti): HECH QACHON
```

### 3. Zaxirali xotira
Asosiy: RAG server (semantik qidiruv)
Zaxira: faylda saqlanadigan markdown ombor (grep bilan qidiruv)
Interfeys: yagona skript — ikkala variant bilan ishlaydi, har doim ikkoviga ham yozadi.

### 4. MCP uchun anti-hallucination qoidalari
- Maʼlumot faqat toolning haqiqiy natijasidan olinadi
- Xato — bu maʼlumot emas: xatoni xabar qiling, raqam oʻylab topmang
- Kesib tashlangan natija — toʻliq maʼlumot emas
- Tekshirmasdan turli VLAN yoki manbalardagi faktlarni aralashtirmang
- Tool natijasi modelning "bilimi"dan ustun

## Arxitektura

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  AI agent   │────▶│ MCP serverlar ×6 │────▶│  Infratuzilma   │
│  (Hermes)   │◀────│  (312 ta tool)   │◀────│  (Proxmox/UniFi/ │
└─────────────┘     └──────────────────┘     │   Sophos/LightRAG)│
                           │                 └─────────────────┘
                           ▼
                    ┌──────────────┐
                    │  Xavfsizlik  │
                    │ (daraja+qoida)│
                    └──────────────┘
```

## Konfiguratsiya misollari

- `config/mcp_servers.yaml` — env oʻzgaruvchilari bilan bir nechta serverning konfiguratsiyasi
- `config/safety_rules.yaml` — harakatlarni xavfsizlik darajasiga boʻlish
- `examples/routed_pattern.py` — routlangan tool chaqiruvlarining tartibi

## Haqiqiy koʻrsatkichlar

| Koʻrsatkich | Qiymat |
|--------|-------|
| MCP serverlar | 6 (unifi, proxmox×3, sophos×2) |
| Jami tool | 312 |
| Serverdagi tool (routing bilan) | 3 tasi koʻrinadi |
| Oʻqitilgandan keyin xavfsizlik buzilishlari | 0/8 test |
| Oʻqitilgandan keyin hallucination | 0% (8/8 test oʻtdi) |

## Litsenziya
MIT

## 📬 Aloqa

Savol boʻlsa yozing: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>
