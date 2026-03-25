# Encrypted Control System using State Encryption

## Overview

This repository presents a simulation framework for a privacy-preserving control system in which only the system state is encrypted, while the feedback gain remains in plaintext.

The goal is to study how encrypted state evolution can be incorporated into a discrete-time feedback control loop while preserving acceptable tracking performance.

This work is part of my M.Tech project in Communication Signal Processing and Machine Learning at IIT Dharwad.

---

## Problem Statement

Consider the discrete-time linear system:

$$
x_{k+1} = A x_k + B u_k
$$

$$
y_k = C x_k + D u_k
$$

In this work, we consider the special case:

$$
C = I, \qquad D = 0
$$

so that the output becomes:

$$
y_k = x_k
$$

A state-feedback control law is used:

$$
u_k = r - Kx_k
$$

Since $y_k = x_k$, the same control law may also be interpreted as output feedback in this special case.

where:
- $x_k$ is the state vector
- $u_k$ is the control input
- $r$ is the reference
- $K$ is the feedback gain matrix

In this version of the project, only the **state vector** is encrypted. The gain \(K\) remains in plaintext.

---

## Why State Encryption Only?

This version focuses on encrypting only the state because:

- it is simpler to implement and explain
- it avoids expensive homomorphic multiplication between encrypted state and encrypted gain
- it provides a clean first step toward privacy-preserving control
- it forms the foundation for a future full-encryption extension

---

## State Encryption Model

The encrypted state evolves recursively as:

$$
V_x[k] = S_x V_x[k-1] + m_x[k] + e[k] \pmod q
$$

where:
- $V_x[k]$: encrypted state
- $S_x$: secret integer matrix
- $m_x[k]$: integer-encoded or quantized state
- $e[k]$: small noise vector
- $q$: large prime modulus

The recovered state is then used to compute the control action with plaintext gain \(K\).

---

## Features

- discrete-time linear system simulation
- plaintext state-feedback control
- recursive state encryption
- modular arithmetic with large prime modulus
- approximate state recovery
- comparison between plaintext and recovered/encrypted-domain behavior

---

## Repository Structure

```text
encrypted-control-system-state-encryption/
├── README.md
├── LICENSE
├── .gitignore
├── matlab/
├── python/
├── docs/
└── results/
