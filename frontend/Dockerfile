# ---------- Stage 1: build ----------
FROM node:20-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# ---------- Stage 2: serve ----------
FROM nginx:alpine

# create non-root user
RUN adduser -D appuser

COPY --from=builder /app/dist /usr/share/nginx/html

#USER appuser

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
