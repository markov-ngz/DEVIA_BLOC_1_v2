# Format CDC message

### Generate JAR file 
Check maven assembly pom xml file 
```
      <plugin>
        <artifactId>maven-assembly-plugin</artifactId>
        <configuration>
        <appendAssemblyId>False</appendAssemblyId> # for a single file 
          <descriptorRefs>
            <descriptorRef>jar-with-dependencies</descriptorRef> # type of packaging the dependencies 
          </descriptorRefs>
          <archive>
              <manifest>
                <addClasspath>true</addClasspath> # add the 'entrypoint'
                <mainClass>com.devia.App</mainClass>
              </manifest>
          </archive>
        </configuration>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>single</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
```
Create a single jar file with dependencies & your code 
```
mvn clean compile package assembly:single
java -jar target\cdc-1.0-SNAPSHOT.jar
```

Extract information from the jar file 
```
jar xf <filename>.jar
```

Build docker file 
```
docker buildx build -t markreduce/etl:kafkacdc .
```