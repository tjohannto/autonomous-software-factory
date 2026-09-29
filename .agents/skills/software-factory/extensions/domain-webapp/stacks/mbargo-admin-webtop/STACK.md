# Tech-Stack Profile: mbargo Admin Webtop

This stack profile specializes the `domain-webapp` overlay for the **mbargo Webtop** application — a server-rendered Java 17 enterprise web application for digital content monitoring and anti-piracy operations.

---

## 🏗️ Architecture & Versions

* **Runtime & Language:** Java 17 LTS.
* **UI & Component Framework:** Apache Wicket 9.22.0 (`wicket-core`, `wicket-extensions`, `wicket-auth-roles`).
  * *Architecture:* Component-based server-side rendering, Model-driven state (`IModel`), HTML/Java file pairs.
* **Build & Lifecycle:** Apache Maven (`pom.xml`).
  * Packaging: WAR (`target/ROOT.war`).
  * Server: Apache Tomcat (`${CATALINA_BASE}/webapps/`).
* **Database & Persistence:** Microsoft SQL Server (JDBC `13.4.0.jre11`), direct DAOs/models, stored procedures in `database/`.
* **Reporting & Serialization:** Apache POI 5.5.1 (Excel/Word generation), Gson 2.14.0.
* **Logging:** SLF4J 2.0.16 + Log4j2 2.24.3.

---

## 📁 Repository Structure

```text
├── pom.xml                  # Maven build configuration
├── database/                # SQL Server schema, stored procedures, functions
├── src/main/
│   ├── java/mbargo/         # Wicket pages, DAOs, models, services, UI components
│   ├── resources/           # Properties, Log4j2 configs, Tomcat context XMLs
│   └── webapp/              # HTML markup, CSS, JS, images, web.xml
└── src/test/java/           # JUnit test cases and WicketTester suites
```

---

## 🔒 Hermetic Build & Verification Commands

| Stage | Command | Wicket Mode | Context XML | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Test Verification** | `mvn clean test -P test` | `development` | `test_context.xml` | Fast unit & WicketTester verification. |
| **Full Build Verification** | `mvn clean install -P test` | `development` | `test_context.xml` | Mandatory before opening a PR. |
| **Production Build** | `mvn clean package -P production` | `deployment` | `productive_context.xml` | Emits `target/ROOT.war` for Tomcat. |

---

## 🧩 Domain Specifics & Reuse Rules

1. **Wicket HTML/Java Pair Alignment:**
   * Every Wicket component (`MyPanel.java`) **MUST** have an accompanying markup file (`MyPanel.html`) in the same package or matching webapp path.
   * `wicket:id` in the HTML must match the component ID in the Java class 1:1.
2. **Model-Driven Development (`IModel`):**
   * Never store raw detached entity objects directly in Wicket components to avoid memory leaks and serialization crashes during session replication. Always use `IModel<T>` (e.g., `LoadableDetachableModel`, `PropertyModel`).
3. **Database & Schema Guard:**
   * Any change to data structures must be mirrored in `database/` (SQL Server scripts/stored procedures).
4. **Excel/Office Reporting (`Apache POI`):**
   * Reuse existing report generators and POI styles in `mbargo/services/` or `mbargo/reporting/`. Do not reinvent cell styling or workbook creation.
