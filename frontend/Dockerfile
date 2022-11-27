FROM node:alpine as build

ENV REACT_APP_API_URL="http://fridget.co:81"

WORKDIR /app
RUN ["yarn", "install"]
COPY . /app
RUN ["yarn", "build"]

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/nginx.conf /etc/nginx/conf.d
EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]
CMD ["yarn", "start"]