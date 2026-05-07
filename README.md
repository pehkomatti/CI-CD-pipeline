# 🔐 DevSecOps Pipeline Project

## 📌 Overview

This project demonstrates how to build a **DevSecOps pipeline** using **GitHub Actions**.  
The primary goal is to automate the software development lifecycle while integrating **security practices at every stage**.

A simple **Python Flask application** is used as the example application to support pipeline implementation and testing.

---

## ⚙️ Pipeline Features

The pipeline includes **Continuous Integration (CI)** and multiple **DevSecOps security controls**, following a *shift-left* approach — introducing security early in development.

### ✅ Core Capabilities:

- **CI Automation**
  - Automatically runs tests on every push and pull request

- **Code Quality (Linting)**
  - Uses `flake8` to enforce coding standards and detect issues early

- **Secret Scanning**
  - Detects sensitive data (API keys, tokens) using Gitleaks

- **Static Application Security Testing (SAST)**
  - Uses CodeQL to identify vulnerabilities in the source code

- **Security Dashboard Integration**
  - Displays findings in GitHub’s *Security → Code scanning alerts*

- **Workflow Automation**
  - Fully automated pipelines using GitHub Actions

---

## 🧠 DevSecOps Focus

The main focus of this project is **not the application itself**, but the **design and implementation of a secure and automated development pipeline**.

The project demonstrates:

- Shift-left security practices  
- Secure CI/CD pipeline design  
- Integration of multiple security tools  
- Real-world DevSecOps workflow structure  

---

## 🤖 AI-Assisted Development

AI Copilot was used as a **supporting tool** during the development of this project.

It assisted with:  
- Guiding pipeline implementation  
- Troubleshooting issues  

> ⚠️ The AI tool was used as a **learning aid**, and all configurations were **reviewed, understood, and implemented step by step**.

---

## 🎯 Outcome

This project represents a **practical implementation of modern DevSecOps practices**, combining automation, security, and continuous integration in a single pipeline.

---
