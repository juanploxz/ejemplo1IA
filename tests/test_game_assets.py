"""Pruebas estructurales del juego que no requieren un navegador."""

import ast
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


class GameAssetsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.html = (ROOT / "neon_dash_v2.html").read_text(encoding="utf-8")

    def test_streamlit_entrypoint_is_valid_python(self) -> None:
        source = (ROOT / "streamlit_app.py").read_text(encoding="utf-8")
        ast.parse(source)
        self.assertIn('Path(__file__).parent / "neon_dash_v2.html"', source)
        self.assertIn("components.html", source)
        self.assertIn('APP_VERSION = "2.2.0"', source)
        self.assertIn("BUILD {APP_VERSION}", source)

    def test_game_contains_every_playable_mode(self) -> None:
        self.assertIn("v2.2 · 5 modos", self.html)
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
        self.assertIn("pointercancel", self.html)
        self.assertIn("keydown", self.html)

    def test_html_has_no_source_outside_its_tags(self) -> None:
        self.assertEqual(self.html.count("<style>"), 1)
        self.assertEqual(self.html.count("</style>"), 1)
        self.assertEqual(self.html.count("<script>"), 1)
        self.assertEqual(self.html.count("</script>"), 1)
        self.assertTrue(self.html.strip().endswith("</script></body></html>"))

    def test_new_attempt_has_a_safe_intro(self) -> None:
        self.assertIn("const INTRO_DISTANCE=1200", self.html)
        self.assertIn("START_GRACE_DISTANCE=1000", self.html)
        self.assertIn("START_GRACE_MS=3000", self.html)
        self.assertIn("generatedTo=INTRO_DISTANCE", self.html)
        self.assertIn("runTime>START_GRACE_MS&&world>safeUntil&&collide()", self.html)

    def test_reset_restores_all_runtime_state(self) -> None:
        reset = self.html.split("function reset()", 1)[1].split("function start()", 1)[0]
        for state in ("world=score=runTime=0", "speed=6", "gravity=1", "held=false", "hazards=[]"):
            with self.subTest(state=state):
                self.assertIn(state, reset)

    def test_only_one_animation_loop_can_run(self) -> None:
        self.assertIn("function start(){if(running)return", self.html)
        self.assertIn("const id=++runId", self.html)
        self.assertIn("if(!running||id!==runId)return", self.html)


if __name__ == "__main__":
    unittest.main()
