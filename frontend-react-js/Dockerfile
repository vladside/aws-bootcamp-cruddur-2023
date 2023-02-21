FROM node:16.18

WORKDIR /app

COPY . .

RUN npm ci
EXPOSE ${PORT}

ENV PORT=3000
CMD ["npm", "start"]
