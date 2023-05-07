import app

class TestFlaskAppWrapper:

    def test_blackAndWhite(pixels):
        assert app.FlaskAppWrapper.transformPixels([
            [[1,2,3]],
            [[4,5,6]]
        ]) == [[2,5]]