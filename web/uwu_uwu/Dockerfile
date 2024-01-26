FROM node:16
COPY ./* /home/node/app/
COPY ./public/* /home/node/app/public/
COPY ./public/texts/* /home/node/app/public/texts/
WORKDIR /home/node/app
RUN npm install
ENV PORT=41343
RUN chown -R node:node /home/node/app
USER node
CMD ["bash", "launch.sh"]
EXPOSE 41343
