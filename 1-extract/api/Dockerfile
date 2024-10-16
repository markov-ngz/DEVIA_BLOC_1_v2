FROM openjdk:24-ea-oraclelinux9
WORKDIR /app
COPY target/api-1.0-SNAPSHOT.jar api.jar
ENTRYPOINT ["java", "-jar", "api.jar"] 