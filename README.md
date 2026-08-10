# PhishX — AI-Powered Scam Detection & Cyber Awareness Platform
### Detect • Explain • Protect
#### Team QUADRANOVA

<p align="center">
  <img src="https://img.shields.io/badge/AI-Powered-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Cybersecurity-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Multilingual-English%20%7C%20Hindi%20%7C%20Kannada-green?style=for-the-badge" />
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

## What Makes PhishX Different?
PhishX goes beyond simple phishing detection by combining **detection, explanation, prevention, reporting, and cybersecurity education** in a single platform.
Its focus is not only on identifying whether content is suspicious, but on helping users understand **why it is suspicious and what they should do next**.

# Problem Statement

Digital scams are becoming increasingly sophisticated, using phishing messages, fake banking alerts, impersonation, malicious links, fraudulent offers, and manipulated digital content to deceive users.

Many users struggle to distinguish legitimate communication from fraudulent content, especially when attacks rely on urgency, authority, emotional manipulation, or familiar brands.

Existing solutions often focus only on detecting threats. Users may receive a warning without understanding:

- Why the content is suspicious
- Which indicators triggered the warning
- What action they should take
- How to report the incident

PhishX addresses this gap by combining AI-based threat detection with explainable analysis, preventive guidance, multilingual accessibility, and cybersecurity education.

# Our Solution

PhishX is an AI-powered cybersecurity platform that helps users identify and understand suspicious digital content.

Users can:

- Paste suspicious messages, emails, or links
- Upload screenshots of conversations, SMS messages, or emails
- Receive an AI-generated risk assessment
- Understand the indicators behind the detection
- Receive actionable safety recommendations
- Generate a structured scam report
- Access cybersecurity awareness resources
- Practice identifying scams through interactive learning

### Core Approach

**Detect → Analyze → Explain → Protect**

Instead of simply telling users that something is dangerous, PhishX explains the potential threat and guides them toward safer action.

# Demo

A demonstration video showcasing the PhishX platform and its core workflows is available below.
🎥 [Watch the PhishX Demo Video] https://drive.google.com/file/d/13FzW7yqSC3vCY2dKbARbHkY90reQmnCk/view?usp=sharing

# Sample Scam Inputs
PhishX can analyse different types of suspicious content, including:

1. Fake banking and KYC messages
2. OTP and account verification scams
3. Malicious or suspicious links
4. Impersonation messages
5. Fake job and investment offers
6. Fraudulent delivery or payment notifications
7. Regional-language scam messages

### Example

> "Your bank account will be blocked within 2 hours. Click the link below to complete your KYC verification."

PhishX analyses indicators such as urgency, impersonation, suspicious URLs, and requests for sensitive information before generating a risk assessment.

1. Dear Customer, your SBI account will be permanently blocked within 2 hours due to incomplete KYC verification. Click here immediately to update your PAN and Aadhaar details:
http://sbi-secure-verify-login.com
Failure to comply may result in account suspension.

2. प्रिय ग्राहक, आपका बैंक खाता 24 घंटे के अंदर बंद कर दिया जाएगा क्योंकि आपका KYC अधूरा है। तुरंत अपना आधार और पैन अपडेट करने के लिए नीचे दिए गए लिंक पर क्लिक करें:
http://secure-kyc-update-bank.in
ध्यान दें: सत्यापन नहीं करने पर आपका खाता फ्रीज कर दिया जाएगा।

3. ಪ್ರಿಯ ಗ್ರಾಹಕರೇ, ನಿಮ್ಮ ಬ್ಯಾಂಕ್ KYC ಪರಿಶೀಲನೆ ಪೂರ್ಣಗೊಂಡಿಲ್ಲ. 2 ಗಂಟೆಗಳೊಳಗೆ ಪರಿಶೀಲನೆ ಮಾಡದಿದ್ದರೆ ನಿಮ್ಮ ಖಾತೆಯನ್ನು ತಾತ್ಕಾಲಿಕವಾಗಿ ಬಂದ್ ಮಾಡಲಾಗುತ್ತದೆ.
ತಕ್ಷಣ ಪರಿಶೀಲಿಸಲು ಕೆಳಗಿನ ಲಿಂಕ್ ಕ್ಲಿಕ್ ಮಾಡಿ:
http://secure-bank-verification.in

4. <img width="501" height="617" alt="image" src="https://github.com/user-attachments/assets/8e9d1fe0-b7da-43eb-9740-877648c4e622" />


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
- HTML5
- CSS3
- JavaScript

## Backend
- Python
- Flask

## AI & Analysis
- Google Gemini API
- OCR
- Image Processing

## Visualization
- Interactive Pentagon Threat Analysis Graph

## Supporting Libraries
- Pillow
- Python OCR libraries
- Google Generative AI SDK


# Key Features

## 🔍 AI-Based Scam Analyzer

PhishX analyses suspicious digital content such as:

- SMS messages
- WhatsApp conversations
- Emails
- OTP requests
- Suspicious links
- Fraudulent notifications
- Uploaded screenshots

The AI engine evaluates the content and generates a risk assessment based on multiple phishing and social-engineering indicators.
### Risk Score
A numerical assessment indicating the severity of the potential threat.
| Risk Score | Threat Level    |
| ---------- | --------------- |
| 0–25       | Low Risk        |
| 26–49      | Suspicious      |
| 50–74      | High Risk       |
| 75–100     | Critical Threat |

## Explainable AI Breakdown

PhishX does not rely only on a "safe" or "dangerous" verdict.
It provides an explanation of the detected risk indicators, helping users understand how social engineering and phishing techniques are being used.

Example indicators include:
* Urgency-based language
* Fake authority impersonation
* OTP extraction attempts
* Suspicious URLs
* Emotional manipulation
* Financial coercion
This ensures transparency and improves cybersecurity awareness among users.
##  Screenshot-Based Scam Analysis
PhishX allows users to upload screenshots of suspicious digital communication instead of manually copying the message.

Supported inputs include:

- Chat screenshots
- SMS screenshots
- Email screenshots
- Fraudulent advertisements

### Workflow

1. User uploads a screenshot
2. OCR extracts relevant text
3. Extracted content is processed
4. Gemini analyses the content
5. PhishX generates a risk assessment and explanation

This makes scam analysis easier for users who may not be comfortable copying or interpreting suspicious messages manually.

##  Pentagon Threat Visualization

PhishX represents the detected threat across five dimensions:

| Dimension | Description |
|---|---|
| Urgency | Pressure to act immediately |
| Technical | Technical deception indicators |
| Social | Emotional or psychological manipulation |
| Trust | Impersonation and credibility signals |
| Intent | Overall malicious intent |

The visualization allows users to understand the threat profile at a glance rather than relying only on a single risk score.

## Preventive Recommendations
Based on the detected threat, PhishX provides practical recommendations such as:

- Avoiding suspicious links
- Not sharing OTPs or sensitive information
- Blocking suspicious senders
- Changing compromised passwords
- Enabling two-factor authentication
- Contacting the official organization directly
- Reporting fraudulent activity

The objective is to move from **detection to prevention**.

## Scam Reporting Assistance
For high-risk content, PhishX assists users in preparing a structured phishing incident report.
Users can:
- Generate a concise incident summary
- Copy the generated report
- Access the appropriate official reporting channel

This reduces the friction involved in reporting suspicious cyber incidents.

# Additional Platform Modules
##  Cybersecurity Awareness Modules
## Scam Awareness Library

Educational resources covering common scams such as:

- UPI scams
- OTP fraud
- Fake job offers
- KYC scams
- QR-code scams
- Investment fraud
- Delivery scams
- Impersonation scams

## Training Lab

A gamified learning environment where users can practise identifying suspicious and legitimate messages, earn XP, and improve their phishing awareness.

## Scam Encyclopedia

A knowledge base explaining different scam categories, attack techniques, warning signs, and preventive measures.

#  Multilingual Accessibility

PhishX supports:
- English
- Hindi
- Kannada

Multilingual support helps make cybersecurity guidance more accessible to users who may be more comfortable interacting in regional languages.
The architecture can be extended to support additional Indian languages in future versions.

# System Workflow
<img width="1380" height="581" alt="WhatsApp Image 2026-05-13 at 15 22 34" src="https://github.com/user-attachments/assets/22d28899-0178-4f20-84d6-d059516cca16" />

# Technology Vision

PhishX follows an **Explainable AI for Cybersecurity** approach.

The platform combines:

- AI-powered analysis
- Explainable threat detection
- Multilingual accessibility
- Cybersecurity education
- Preventive recommendations
- Simplified reporting

The goal is to make cybersecurity assistance understandable and actionable for everyday digital users.

# Competitive Advantages

| Capability | PhishX |
|---|---|
| AI-based scam detection | ✅ |
| Screenshot analysis | ✅ |
| OCR integration | ✅ |
| Explainable AI | ✅ |
| Risk scoring | ✅ |
| Threat visualization | ✅ |
| Preventive recommendations | ✅ |
| Scam reporting assistance | ✅ |
| Multilingual accessibility | ✅ |
| Cybersecurity learning | ✅ |
| Scam knowledge base | ✅ |

# Real-World Applications

PhishX can be applied in:

- Educational institutions
- Digital literacy programs
- Banking awareness initiatives
- Public cybersecurity campaigns
- Small-business security training
- Community awareness workshops

### Target Users

- Students
- Senior citizens
- First-time internet users
- Digital payment users
- Small businesses
- General smartphone users

# Privacy & Security Considerations

PhishX follows a privacy-conscious approach:

- Uploaded screenshots are not intended for permanent storage
- Analysis is performed for the current session
- API credentials are kept outside the source code
- User data collection is minimized
- Sensitive information should not be intentionally submitted

Future versions can introduce stronger privacy controls, secure storage policies, and additional data-protection mechanisms.

# Future Scope

Future versions of PhishX can expand the platform with:

- AI-based deepfake and manipulated-media detection
- Browser extension for real-time webpage analysis
- Real-time URL reputation checking
- Mobile application
- Voice phishing detection
- AI cybersecurity assistant
- Community-reported scam intelligence
- Additional Indian languages
- Real-time scam trend analysis
- Integration with cybersecurity awareness campaigns

These enhancements can evolve PhishX from a phishing analysis platform into a broader AI-powered digital fraud protection system.

# Why PhishX Matters

Cybersecurity tools should not only identify threats — they should help users understand and respond to them.

PhishX bridges the gap between:

**AI-powered threat detection**
+
**Explainable cybersecurity guidance**
+
**User awareness**

Instead of simply warning users about a potential scam, PhishX helps them understand the warning signs and take appropriate action.

# Conclusion

PhishX is an AI-powered cybersecurity awareness platform designed to help users:

- Detect suspicious digital content
- Understand why it may be dangerous
- Receive practical safety recommendations
- Report suspicious activity
- Improve cybersecurity awareness

By combining AI analysis, OCR, explainable results, multilingual support, threat visualization, and interactive learning, PhishX aims to make digital safety more accessible to everyday users.

### Detect. Explain. Protect.

# License
This project is developed and maintained by Team QUADRANOVA.
See the repository license file for usage and distribution terms.


## PhishX
**Detect. Explain. Protect.**
