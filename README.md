# PhishX — AI-Powered Phishing Detection & Cyber Awareness Platform
### Built for ZYNEX Hackathon 2026
#### Team QUADRANOVA

<p align="center">
  <img src="https://img.shields.io/badge/AI-Powered-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Cybersecurity-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Multilingual-English%20%7C%20Hindi%20%7C%20Kannada-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ZYNEX-2026-purple?style=for-the-badge" />
</p>

# Overview
Phishing and social engineering attacks have evolved into one of the most widespread cybersecurity threats affecting individuals and organisations alike. Fraudulent SMS messages, fake banking alerts, malicious links, impersonation scams, and OTP thefts continue to target users who often lack the technical expertise to identify them in time.
**PhishX** is an AI-powered phishing detection and cyber awareness platform designed to help users instantly analyse suspicious messages and screenshots using intelligent threat analysis.

The platform not only detects potential scams, but also:
* Explains why the content is suspicious
* Provides actionable prevention measures
* Educates users through interactive learning modules
* Encourages scam reporting through streamlined workflows

PhishX combines cybersecurity, explainable AI, multilingual accessibility, and user education into a single unified solution.

# Problem Statement
Modern phishing attacks increasingly rely on
* Psychological manipulation
* Impersonation tactics
* Urgency-driven messaging
* Technical deception
* Regional language targeting

Most users:
* Cannot accurately identify phishing attempts
* Do not understand the warning signs
* Lack access to simplified cybersecurity tools
* Hesitate to report incidents due to complexity

Existing solutions are often:
* Too technical for general users
* Limited to spam filtering
* Lacking explainability
* Focused only on detection rather than prevention and awareness

# Our Solution
PhishX addresses these challenges through an AI-driven platform capable of analysing both text-based and image-based phishing attempts. Users can:
* Paste suspicious text messages
* Upload screenshots of chats, emails, or SMS messages
* Receive an AI-generated risk assessment
* Understand the reasoning behind the detection
* Access preventive recommendations
* Learn about scams through educational modules
* Report scams more efficiently

# Demo 
🎥 [Watch the PhishX Demo Video]
https://drive.google.com/file/d/13FzW7yqSC3vCY2dKbARbHkY90reQmnCk/view?usp=sharing
# Installation/Setup
## Clone the Repository
```bash
git clone https://github.com/QUADRANOVA/PhishX.git
cd phishx
```
## Install Dependencies
```bash
pip install -r requirements.txt
```
## Configure API Key
Open `app.py` and replace:
```python
GEMINI_API_KEY = "ADD YOUR GEMINI API KEY HERE"
```
with your actual Gemini API key.

## Run the Application
```bash
python app.py
```
The application will run locally at:
```txt
http://127.0.0.1:5000
```
# Tech Stack

## Frontend
* HTML
* CSS
* JavaScript

## Backend
* Python
* Flask

## AI & Processing
* Google Gemini API
* OCR-based text extraction

## Visualization
* Pentagon threat analysis graph


# Key Features
## 🔍 AI-Based Scam Analyzer
Users can submit:

* SMS messages
* WhatsApp conversations
* Emails
* OTP requests
* Fraudulent links
* Suspicious notifications
The AI engine evaluates the content and generates:
### Risk Score
A numerical assessment indicating the severity of the potential threat.
| Risk Score | Threat Level    |
| ---------- | --------------- |
| 0–25       | Low Risk        |
| 26–49      | Suspicious      |
| 50–74      | High Risk       |
| 75–100     | Critical Threat |
##  Explainable AI Breakdown
Rather than providing only a classification result, PhishX explains:
* Why the content was flagged
* Which phishing indicators were detected
* Keywords and manipulation patterns identified
* Social engineering techniques involved

Example indicators include:
* Urgency-based language
* Fake authority impersonation
* OTP extraction attempts
* Suspicious URLs
* Emotional manipulation
* Financial coercion
This ensures transparency and improves cybersecurity awareness among users.
##  Screenshot-Based Scam Detection
PhishX supports screenshot uploads for analysing:
* Chat screenshots
* SMS captures
* Email screenshots
* Fraudulent advertisements
Workflow:
1. OCR extracts textual content from the image
2. AI analyses the extracted data
3. A detailed phishing assessment is generated
This improves accessibility for users who may not be comfortable manually copying text.
##  Pentagon Threat Visualisation
The platform generates a pentagonal threat graph based on five critical phishing dimensions:
| Dimension | Description                              |
| --------- | ---------------------------------------- |
| Urgency   | Pressure to act immediately              |
| Technical | Technical deception indicators           |
| Social    | Emotional/social manipulation            |
| Trust     | Impersonation of authority or legitimacy |
| Intent    | Overall malicious intent                 |

This provides users with a more intuitive understanding of the threat profile.
## Preventive Recommendations
PhishX provides actionable mitigation steps based on the detected threat level. Examples include:
* Changing passwords
* Enabling two-factor authentication
* Blocking suspicious senders
* Avoiding malicious links
* Contacting banking support
* Reporting fraudulent activity
The goal is not only detection, but also proactive damage prevention.
## Scam Reporting Assistance
If the calculated risk score is **50 or higher**, users can:
* Copy an AI-generated phishing incident report
* Automatically open the official Chakshu reporting portal in a new tab
This simplifies and accelerates cybercrime reporting workflows.

# Additional Platform Modules
##  Scam Awareness Library
The landing page includes curated awareness resources covering:
* UPI scams
* OTP fraud
* Fake job offers
* KYC scams
* QR code scams
* Investment fraud
* Delivery scams
* Deepfake-related scams
This promotes preventive cybersecurity education.

##  Training Lab
The platform includes a gamified cybersecurity learning environment where users can:
* Participate in scam identification challenges
* Differentiate between safe and malicious messages
* Earn XP points
* Improve phishing awareness interactively

This module increases user engagement while reinforcing practical cybersecurity skills.
## Scam Encyclopedia
A dedicated knowledge base allowing users to:
* Explore various scam categories
* Understand attack methodologies
* Learn preventive strategies
* Study real-world phishing examples

#  Multilingual Accessibility
PhishX currently supports:
* English
* Hindi
* Kannada
By supporting regional languages, the platform aims to improve cybersecurity accessibility for a broader audience, including first-time internet users and non-English-speaking communities.

# System Workflow
<img width="1380" height="581" alt="WhatsApp Image 2026-05-13 at 15 22 34" src="https://github.com/user-attachments/assets/22d28899-0178-4f20-84d6-d059516cca16" />

# Technology Vision
PhishX is designed around the concept of **Explainable AI for Public Cybersecurity**. The platform focuses on:
* Accessibility
* Simplicity
* Educational value
* Real-world applicability
* User trust
Rather than functioning solely as a detection engine, PhishX aims to create a complete cybersecurity awareness ecosystem.

# Competitive Advantages

| Capability                      | PhishX |
| ------------------------------- | ------ |
| AI-based phishing detection     | ✅      |
| Screenshot analysis             | ✅      |
| OCR integration                 | ✅      |
| Explainable AI outputs          | ✅      |
| Preventive recommendations      | ✅      |
| Gamified cybersecurity learning | ✅      |
| Educational scam encyclopedia   | ✅      |
| Scam reporting support          | ✅      |
| Multilingual accessibility      | ✅      |
| Visual threat analysis          | ✅      |

# Real-World Applications
PhishX can be applied across:
* Educational institutions
* Banking awareness programs
* Public cybersecurity campaigns
* Digital literacy initiatives
* Small business security training
* Community awareness workshops

Target beneficiaries include:
* Students
* Senior citizens
* Rural internet users
* Digital payment users
* First-time smartphone users

# Privacy & Security Considerations
PhishX follows a privacy-conscious design approach:
* Uploaded screenshots are not permanently stored
* Analysis remains session-based
* Minimal data retention principles are followed
* User safety and confidentiality remain priorities

# Future Scope
Planned future enhancements include:
* Browser extension integration
* Mobile application deployment
* Real-time URL scanning
* Voice phishing detection
* Community-reported scam datasets
* AI chatbot assistance
* Integration with cybersecurity awareness campaigns
* Adding additional languages in the future

# Why PhishX Matters
Cybersecurity tools should not only detect threats, but also empower users to understand and respond to them. PhishX bridges the gap between:
* Advanced AI-based detection
* User-friendly cybersecurity education

The platform combines:
* AI
* Cybersecurity
* Accessibility
* Education
* User engagement
* Social impact

# Conclusion
PhishX is more than a phishing detection tool. It is a proactive cybersecurity awareness platform designed to:
* Detect threats
* Educate users
* Encourage preventive action
* Simplify scam reporting
* Improve digital safety accessibility
By combining intelligent analysis with explainable insights and multilingual support, PhishX aims to make cybersecurity understandable and accessible for everyone.
# License
This project was developed for ZYNEX Hackathon 2026 by Team QUADRANOVA.
# "Detect the scam before it detects you."
## PhishX — Team QUADRANOVA
