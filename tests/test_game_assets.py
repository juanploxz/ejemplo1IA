"""Pruebas estructurales del juego que no requieren un navegador."""

import ast
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class GameAssetsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.html = (ROOT / "game.html").read_text(encoding="utf-8")

    def test_streamlit_entrypoint_is_valid_python(self) -> None:
        source = (ROOT / "streamlit_app.py").read_text(encoding="utf-8")
        ast.parse(source)
        self.assertIn('Path(__file__).parent / "game.html"', source)
        self.assertIn("components.html", source)

    def test_game_contains_every_playable_mode(self) -> None:
        for mode in ("cube", "ship", "ball", "wave", "ufo"):
            with self.subTest(mode=mode):
                self.assertIn(f"'{mode}'", self.html)

    def test_procedural_mechanics_are_present(self) -> None:
        for mechanic in ("function generate()", "function addGate", "gravity", "speed", "boost"):
            with self.subTest(mechanic=mechanic):
                self.assertIn(mechanic, self.html)

    def test_canvas_and_touch_controls_are_available(self) -> None:
        self.assertIn('<canvas id="game"', self.html)
        self.assertIn("pointerdown", self.html)
        self.assertIn("keydown", self.html)


if __name__ == "__main__":
    unittest.main()
