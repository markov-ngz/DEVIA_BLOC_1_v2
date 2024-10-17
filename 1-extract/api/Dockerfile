FROM openjdk:24-slim-bookworm
WORKDIR /app
COPY target/api-1.0-SNAPSHOT.jar api.jar
ENTRYPOINT ["java", "-jar", "api.jar"] 