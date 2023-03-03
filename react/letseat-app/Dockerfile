# For more information, please refer to https://aka.ms/vscode-docker-python
FROM node:14

WORKDIR /app

# Copy package.json and package-lock.json files into the container
COPY package*.json ./

# Copy the frontend code into the container
COPY . .

# Build the React App
RUN npm run build

ENV PUBLIC_URL = /static
WORKDIR /app/build

# Expose port to run frontend on 
EXPOSE 3000

# Start frontend
CMD ["npm", "start"]