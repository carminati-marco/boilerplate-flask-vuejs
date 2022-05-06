# Choose the Image which has Node installed already
FROM node:lts-alpine

# install simple http server for serving static content
RUN npm install -g http-server

# make the 'app' folder the current working directory
WORKDIR /app


# copy both 'package.json' and 'package-lock.json' (if available)
COPY  client/package*.json .

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY  client/. .

# build app for production with minification

ARG VUE_APP_REST_URL                       
ENV VUE_APP_REST_URL=$VUE_APP_REST_URL 

RUN npm run build

EXPOSE 8080
CMD [ "http-server", "dist" ]