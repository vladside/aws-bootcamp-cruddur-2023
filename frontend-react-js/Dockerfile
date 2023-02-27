FROM node:16.18

WORKDIR /node
COPY package.json package-lock.json ./

RUN npm ci

WORKDIR /node/app
COPY . .

RUN chmod +x start.sh

EXPOSE ${PORT}

ENV PORT=3000
CMD [ "./start.sh"]
