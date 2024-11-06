# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /myapp

# Copy the requirements.txt first to install dependencies
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port your application runs on (optional)
EXPOSE 5000

# Set the default command to run your Python application
CMD ["python", "app.py"]

