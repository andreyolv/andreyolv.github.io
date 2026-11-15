(() => {
  const catalog = document.getElementById("portfolio-catalog");
  if (!catalog) return;

  const rows = Array.from(catalog.querySelectorAll("tbody tr[data-status]"));
  const filters = Array.from(catalog.querySelectorAll(".portfolio-filter"));
  const noResults = catalog.querySelector(".portfolio-no-results");
  const state = { status: "all", environment: "all" };

  const values = {};
  filters.forEach((group) => {
    values[group.dataset.filterGroup] = new Set(
      Array.from(group.querySelectorAll("button[data-filter-value]")).map(
        (button) => button.dataset.filterValue
      )
    );
  });

  const params = new URLSearchParams(window.location.search);
  for (const key of Object.keys(state)) {
    const value = params.get(key);
    if (value && values[key] && values[key].has(value)) {
      state[key] = value;
    }
  }

  function updateCounts() {
    filters.forEach((group) => {
      const key = group.dataset.filterGroup;
      const otherKey = key === "status" ? "environment" : "status";
      group.querySelectorAll("button[data-filter-value]").forEach((button) => {
        const value = button.dataset.filterValue;
        const count = rows.filter((row) => {
          const matchesOther =
            state[otherKey] === "all" ||
            row.dataset[otherKey] === state[otherKey];
          const matchesSelf =
            value === "all" || row.dataset[key] === value;
          return matchesOther && matchesSelf;
        }).length;
        const countElement = button.querySelector(".portfolio-filter__count");
        if (countElement) countElement.textContent = String(count);
      });
    });
  }

  function apply(updateUrl) {
    let visible = 0;
    rows.forEach((row) => {
      const show =
        (state.status === "all" || row.dataset.status === state.status) &&
        (state.environment === "all" ||
          row.dataset.environment === state.environment);
      row.hidden = !show;
      if (show) visible += 1;
    });

    if (noResults) noResults.hidden = visible > 0;

    filters.forEach((group) => {
      const key = group.dataset.filterGroup;
      group.querySelectorAll("button[data-filter-value]").forEach((button) => {
        const active = button.dataset.filterValue === state[key];
        button.classList.toggle("is-active", active);
        button.setAttribute("aria-pressed", String(active));
      });
    });

    updateCounts();

    if (updateUrl) {
      const url = new URL(window.location.href);
      for (const key of Object.keys(state)) {
        if (state[key] === "all") url.searchParams.delete(key);
        else url.searchParams.set(key, state[key]);
      }
      window.history.replaceState(null, "", url.toString());
    }
  }

  filters.forEach((group) => {
    group.addEventListener("click", (event) => {
      const button = event.target.closest("button[data-filter-value]");
      if (!button) return;
      state[group.dataset.filterGroup] = button.dataset.filterValue;
      apply(true);
    });
  });

  apply(true);
})();
