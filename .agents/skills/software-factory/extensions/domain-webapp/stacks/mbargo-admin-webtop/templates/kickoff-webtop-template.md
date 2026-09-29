# Kick-off: [Story Name] (mbargo Webtop)

## 🎯 Goal
[Concise 1-sentence description of the feature, panel, or report]

## 📐 Interface Skeleton (Mandatory Contract)
```java
// Define Wicket Page/Panel and Model interfaces
public class TargetPanel extends Panel {
    public TargetPanel(String id, IModel<TargetModel> model) {
        super(id, model);
    }
}
```

## 🧩 Reusable Webtop Components & Services
* **Existing Wicket Base Classes:** `mbargo.ui.base.BasePage`, `mbargo.ui.components.*`
* **DAO / Model Services:** `mbargo.services.*`, `mbargo.dao.*`
* **Reporting:** Existing POI Excel exporters in `mbargo.reporting.*`

## 🔒 Hermetic Environment & Constraints
* **Build Profile:** `mvn clean install -P test` (Wicket mode: development, uses `test_context.xml`).
* **Markup Rule:** Every `wicket:id` in HTML must match Java component hierarchy 1:1.
* **Model Rule:** Wrap entities in `IModel` (e.g. `LoadableDetachableModel`). Never hold direct entity references in component fields.
