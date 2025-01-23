    <build>
        <plugins>
            <!-- Spring Boot Maven Plugin -->
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <version>2.1.2.RELEASE</version> <!-- Явная версия -->
            </plugin>

            <!-- SonarQube Maven Plugin -->
            <plugin>
                <groupId>org.sonarsource.scanner.maven</groupId>
                <artifactId>sonar-maven-plugin</artifactId>
                <version>${sonar.maven.plugin.version}</version>
            </plugin>
        </plugins>
    </build>

