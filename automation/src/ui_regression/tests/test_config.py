"""Tests for UI regression environment configuration."""

from automation.src.ui_regression.config import UiRegressionConfig


def test_direct_mode_reads_local_service_urls(monkeypatch):
    monkeypatch.setenv("UI_REGRESSION_DIRECT", "1")
    monkeypatch.setenv("UI_REGRESSION_BACKEND_URL", "http://127.0.0.1:9400")
    monkeypatch.setenv("UI_REGRESSION_AI_URL", "http://127.0.0.1:9411")
    monkeypatch.setenv("UI_REGRESSION_DB_LOCAL_PORT", "3306")

    config = UiRegressionConfig.from_env()

    assert config.direct is True
    assert config.backend_url == "http://127.0.0.1:9400"
    assert config.ai_url == "http://127.0.0.1:9411"
    assert config.db_local_port == 3306
