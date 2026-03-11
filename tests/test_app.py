import pytest
import app


def test_header_present(dash_duo):
    dash_duo.start_server(app.app)

    header = dash_duo.find_element("h1")

    assert header.text != ""


def test_graph_present(dash_duo):
    dash_duo.start_server(app.app)

    graph = dash_duo.find_element("#sales-line-chart")

    assert graph is not None


def test_region_filter_present(dash_duo):
    dash_duo.start_server(app.app)

    dropdown = dash_duo.find_element("#region-filter")

    assert dropdown is not None