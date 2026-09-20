#!/usr/bin/env bash
set -e

echo "Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y falkon thunar synaptic codelite pulseaudio pavucontrol 

echo "setting up audio" 

