FROM node:16.18 as builder_package_files

WORKDIR /node
COPY package.json package-lock.json ./

RUN npm ci

FROM node:16.18 as builder

WORKDIR /node/app
COPY . .

COPY --from=builder_package_files /node ./

RUN chmod +x start.sh

EXPOSE ${PORT}

ENV PORT=3000
CMD [ "./start.sh"]
