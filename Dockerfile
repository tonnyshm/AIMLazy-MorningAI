# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /frontend/pages/index.js

# Copy package.json and package-lock.json
COPY package*.json ./

# Install any needed packages
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run your app
CMD ["node", "app.js"]