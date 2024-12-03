FROM node:23-slim

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm install --include=dev

COPY . .
