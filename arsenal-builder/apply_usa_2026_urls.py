"""Write the researched project URLs into the USA 2026 tool files."""
import json
import os

DEST = "../tools/USA/2026"

URLS = {
    "AC Scanner - QubitAC Automated Post-Quantum Cryptography Discovery Tool": "https://github.com/qubitac/AC-Scanner",
    "AD Miner – One step further applying graph theory for Active Directory security analysis": "https://github.com/AD-Security/AD_Miner",
    "AI Attack & Defence Wargame: The Insurance Company Edition": "https://play.secdim.com/",
    "APTL: Advanced Purple Team Labs": "https://github.com/Brad-Edwards/aptl",
    "ARAY: Benign Binary Synthesis for Signature Validation Without the Malware": "https://github.com/c2dc/aray",
    "AgentsLeak: Runtime Protection for AI Coding Agents": "https://github.com/IngaCherny/AgentsLeak",
    "Anthropic-Cybersecurity-Skills": "https://github.com/mukul975/Anthropic-Cybersecurity-Skills",
    "Azazel-Edge : Deterministic Edge Decision Support for Constrained SOC/NOC Operations": "https://github.com/01rabbit/Azazel-Edge",
    "BadZure: Building Cloud Attack Labs with AI": "https://github.com/mvelazc0/BadZure",
    "Bastet: An Infrastructure for Benchmarking LLM Smart Contract Auditing": "https://github.com/OneSavieLabs/Bastet",
    "Bedrock Keys Security (BKS): Hunting Phantom IAM Users Created by AWS Bedrock API Keys": "https://github.com/BeyondTrust/bedrock-keys-security",
    "Brutus: Modern Multi-Protocol Credential Testing in Go": "https://github.com/praetorian-inc/brutus",
    "CLOAK : Cloud Testing Agent Harness": "https://github.com/openrec0n/cloak",
    "Chameleon Forensics (Android): Assume Adversarial Logical Extraction Forensic Tool": "https://github.com/Ins1ght32/Chameleon-Forensics-Android",
    "Chef Special: Updates to CSTC - CyberChef-inspired Message Transformator in BurpSuite": "https://github.com/usdAG/cstc",
    "ConfigManBearPig - Identify, Visualize, and Navigate SCCM Attack Paths in BloodHound": "https://github.com/SpecterOps/ConfigManBearPig",
    "Continuous Threat Modeling in Agentic AI era - tmdd": "https://github.com/attasec/tmdd",
    "CrowdSentinel: AI-Orchestrated Threat Hunting Across Unified Security Data Sources": "https://github.com/thomasxm/CrowdSentinels-AI-MCP",
    "CyberArkHound": "https://github.com/jazofra/CyberArkHound",
    "Dradis Framework: Intelligent Automation for collaboration and reporting": "https://github.com/dradis/dradis-ce",
    "EMBA – The product security analysis framework": "https://github.com/e-m-b-a/emba",
    "EMBArk – Firmware Analysis for the Enterprise": "https://github.com/e-m-b-a/embark",
    "Emulate cloud-native attacks with Stratus Red Team": "https://github.com/DataDog/stratus-red-team",
    "FAInd my XPC: Automated Discovery of Privilege Escalation via macOS XPC Trust Boundaries - powered by LLM": "https://github.com/XMCyber/FAInd-my-xpc",
    "From Breakthrough to Completeness: arkdecompiler - The Decompiler for HarmonyOS NEXT": "https://github.com/jd-opensource/arkdecompiler",
    "Ghostwriter": "https://github.com/GhostManager/Ghostwriter",
    "GolemHalt: A Deterministic Reference Monitor for AI Coding Agents": "https://github.com/sondera-ai/sondera-coding-agent-hooks",
    "Hecate: a trivial UART tool": "https://github.com/tigard-tools/hecate",
    "HoneyMCP: A Deception Security Layer for MCP Servers": "https://github.com/barvhaim/HoneyMCP",
    "ICSForge™: OT/ICS Security Coverage Validation Platform": "https://github.com/ICSForge/ICSForge",
    "Intercept.js: Context-Aware YARA for Runtime Detection In JavaScript Environments": "https://github.com/rishi-sekantsec/sekant-intercept-js",
    "JS-Tap v3: JavaScript Post-Exploitation Moves to the Endpoint": "https://github.com/hoodoer/JS-Tap",
    "KEIP: Kernel-Enforced Install-Time Policies": "https://github.com/Otsmane-Ahmed/KEIP",
    "Keychecker : SSH Key based attack tool for DVCS Systems": "https://github.com/cyfinoid/keychecker",
    "LLM Hacking 101": "https://github.com/RootInj3c/LLM-Playground",
    "LoRaCraft – Crafting Attacks for LoRaWAN Networks": "https://github.com/pinarsadioglu/loracraft",
    "LogonTracer v2: Faster Malicious Windows Logon Investigations with AI Agent": "https://github.com/JPCERTCC/LogonTracer",
    "MCParasite: Universal MCP Worm Security Testing Framework": "https://github.com/MCParasite/mcparasite",
    "MEM-SBOM: Runtime SBOM Generation from Python Process Memory": "https://github.com/HalaAli198/MEM-SBOM",
    "MLOKit: MLOps Attack Toolkit": "https://github.com/h4wkst3r/MLOKit",
    "MORF - Mobile Reconnaissance Framework": "https://github.com/amrudesh1/morf",
    "MSCodePhish - Dynamic Device Code Phishing Framework": "https://github.com/TROUBLE-1/MSCodePhish",
    "MSSQLHound - Identify, Visualize, and Navigate MSSQL Attack Paths in BloodHound": "https://github.com/SpecterOps/MSSQLHound",
    "MachStealer:One Pipeline Behind Every macOS Infostealer": "https://github.com/ultra-supara/MachStealer",
    "Mecha Hayabusa by Yamato Security": "https://github.com/Yamato-Security/mecha-hayabusa",
    "Medaudit, an AI assisted Tool for Auditing Hospital Networks and Pentesting Medical Devices": "https://github.com/anirudhduggal/medaudit",
    "Nemesis 2.2": "https://github.com/SpecterOps/Nemesis",
    "OWASP EKS Goat: Hands-On AWS EKS Security": "https://github.com/OWASP/www-project-eks-goat",
    "OWASP Faction 2.0": "https://github.com/factionsecurity/faction",
    "PETriage: Cross-Platform PE Surface Analysis for Malware Triage": "https://github.com/uky007/PETriage",
    "Pathrunner: An AWS Privilege Escalation Framework": "https://github.com/DataDog/pathrunner",
    "Pentest Copilot V2: The Agentic Pentesting Workspace": "https://github.com/bugbasesecurity/pentest-copilot",
    "Practical Ransomware Detection on macOS (via Math, not AI)": "https://github.com/objective-see/RansomWhere",
    "Praxis - Semantic Command & Control Framework": "https://github.com/originsec/praxis",
    "Precogly: Open Source Threat Modeling for AI-Assisted Security": "https://github.com/precogly/precogly",
    "PrivacyTrollShield: An Open-Source Scanner for Privacy Compliance": "https://github.com/atekippe/PrivacyTrollShield",
    "PwnSat 2.0: The Vulnerable Satellite Hacking Platform for Learning Through Research": "https://github.com/r0r0x-xx/PwnSat-2.0",
    "QuicDraw & QuicDraw-UI: Racing and Fuzzing HTTP/3": "https://github.com/cyberark/QuicDrawH3",
    "ROP ROCKET: New ASLR Bypass Mini-Tool & Automating Advanced ROP Attacks": "https://github.com/Bw3ll/ROP_ROCKET",
    "ReARM: Release Governance Platform": "https://github.com/relizaio/rearm",
    "RedTeamSimmer: A Web Based Adversary Emulation Platform and Atomic Red Team Test Orchestration": "https://github.com/BreachSimRange/RedTeamSimmer",
    "SBoMPlay : SBoM Exploration and Intelligence extraction platform": "https://github.com/cyfinoid/sbomplay",
    "SEmuRAI: Software Emulation and Reversing AI Agent": "https://github.com/DevNerdGR/SEmuRAI-mcp",
    "SHAREM: Next-Generation Shellcode Analysis Tool": "https://github.com/Bw3ll/sharem",
    "Sage: Giving an AI the Keys to Your C2 Framework": "https://github.com/MythicAgents/sage",
    "ShadowHunt 2.0: Uncovering Shadow IT and Hidden Secrets": "https://github.com/cooltoolz/ShadowHunt2.0",
    "ShellWasp: Creating Shellcode with Windows Syscalls": "https://github.com/Bw3ll/ShellWasp",
    "Splunk MCP LLM SIEMulator: Open Source AI Security Monitoring Through Model Context Protocol Integration": "https://github.com/rsfl/splunk-mcp-llm-siemulator",
    "StegoScan": "https://github.com/LCBOWER33/StegoScan",
    "Surfactant - Modular Framework for File Information Extraction and SBOM Generation": "https://github.com/LLNL/Surfactant",
    "Suricata 8: Discover the Difference in Network Detection": "https://github.com/OISF/suricata",
    "Suricata Turbo: Let Your NIC Drop the Flows Suricata Won't Miss": "https://github.com/DynaNIC/suricata-turbo",
    "Suzaku by Yamato Security": "https://github.com/Yamato-Security/suzaku",
    "TSURUGI LINUX - the sharpest weapon in your DFIR arsenal": "https://tsurugi-linux.org/",
    "Tengu Marauder Vanguard Version 2.0": "https://github.com/Lexicon121/Tengu-Marauder-Vanguard",
    "The Metasploit Framework 6.5: Malleable C2 Payloads, New Relay Capability and Protocol Session Upgrades": "https://github.com/rapid7/metasploit-framework",
    "ThreatShield - The Intelligent Way of Threat Modelling": "https://github.com/threatshield/threatshield",
    "ThreatXtension: AI-Powered Browser Extension Security Analysis Framework": "https://github.com/barvhaim/ThreatXtension",
    "Trajan: Cross-Platform CI/CD Security Scanner": "https://github.com/praetorian-inc/trajan",
    "VulnZoo: A Complete Vulnerable IoT Ecosystem for Security Research and Training": "https://github.com/DEKRA-Cybersecurity/VulnZoo",
    "Vulnhalla 2.0: LLM-Guided Triage of CodeQL Findings": "https://github.com/cyberark/Vulnhalla",
    "WebAgentAudit: Security Auditing of Web-Based AI Agents Through Browser Automation": "https://github.com/atom41research/webagentaudit",
    "capa: Beyond Disassembly: Dynamic Matching for Static Blindspots": "https://github.com/mandiant/capa",
    "fetter": "https://github.com/fetter-io/fetter-rs",
    "findmytakeover - find dangling domains in a multi cloud environment": "https://github.com/anirudhbiyani/findmytakeover",
    "notyet: Automated IAM Persistence Analysis Through AWS Eventual Consistency Abuse": "https://github.com/OFFENSAI/notyet",
    "pymsi - Interactive MSI Installer Analysis in Python and the Browser": "https://github.com/nightlark/pymsi",
    "unrelabel: how to destroy an ML model": "https://github.com/oz9un/unrelabel",
    "xEndity": "https://github.com/kenleejl/xEndityv2",
}


def main():
    seen = set()
    for f in sorted(os.listdir(DEST)):
        if not f.endswith(".json"):
            continue
        path = os.path.join(DEST, f)
        d = json.load(open(path, encoding="utf-8"))
        url = URLS.get(d["Tool Name"])
        if url:
            d["Github URL"] = url
            seen.add(d["Tool Name"])
            json.dump(d, open(path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    missing_key = set(URLS) - seen
    if missing_key:
        print("⚠️  URLs with no matching tool file:")
        for m in sorted(missing_key):
            print("   ", m)
    print(f"✅ Applied {len(seen)} URLs")


if __name__ == "__main__":
    main()
