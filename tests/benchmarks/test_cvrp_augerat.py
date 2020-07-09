import sys

sys.path.append("../../vrpy/")

from examples.benchmarks.cvrp_augerat import DataSet


class TestsAugerat:

    def setup(self):
        """
        Augerat instance P-n16-k8.vrp
        """
        self.data = DataSet(path="../examples/benchmarks/data/",
                            instance_name="P-n16-k8.vrp")
        self.G = self.data.G

    def test_setup_instance_name(self):
        assert self.G.graph["name"] == "P-n16-k8"

    def test_setup_vehicle_capacity(self):
        assert self.G.graph["vehicle_capacity"] == 35

    def test_setup_nodes(self):
        # extra node for the Sink
        assert len(self.G.nodes()) == 16 + 1

    def test_setup_edges(self):
        assert len(self.G.edges()) == 16 * (16 - 1) + 1

    def test_subproblem_lp(self):
        self.data.solve()
        assert round(self.data.best_value, -1) in [450, 460]

    def test_subproblem_lp_dive(self):
        self.data.solve(dive=True)
        assert round(self.data.best_value, -1) in [450, 460]

    def test_subproblem_lp_greedy(self):
        self.data.solve(greedy=True)
        assert round(self.data.best_value, -1) in [450, 460]

    def test_subproblem_lp_greedy_dive(self):
        self.data.solve(greedy=True, dive=True)
        assert round(self.data.best_value, -1) in [450, 460]

    def test_subproblem_cspy(self):
        self.data.solve(cspy=True)
        assert round(self.data.best_value, -1) in [450, 460]

    def test_subproblem_cspy_dive(self):
        self.data.solve(cspy=True, dive=True)
        assert round(self.data.best_value, -1) in [450, 460]

    def test_subproblem_lp_with_initial_routes(self):
        # benchmark result
        # http://vrp.galgos.inf.puc-rio.br/index.php/en/
        r_1 = ["Source", 2, "Sink"]
        r_2 = ["Source", 6, "Sink"]
        r_3 = ["Source", 8, "Sink"]
        r_4 = ["Source", 15, 12, 10, "Sink"]
        r_5 = ["Source", 14, 5, "Sink"]
        r_6 = ["Source", 13, 9, 7, "Sink"]
        r_7 = ["Source", 11, 4, "Sink"]
        r_8 = ["Source", 3, 1, "Sink"]
        ini = [r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8]
        self.data.solve(initial_routes=ini)
        assert int(self.data.best_value) == 450

    def test_subproblem_lp_with_initial_routes_dive(self):
        # benchmark result
        # http://vrp.galgos.inf.puc-rio.br/index.php/en/
        r_1 = ["Source", 2, "Sink"]
        r_2 = ["Source", 6, "Sink"]
        r_3 = ["Source", 8, "Sink"]
        r_4 = ["Source", 15, 12, 10, "Sink"]
        r_5 = ["Source", 14, 5, "Sink"]
        r_6 = ["Source", 13, 9, 7, "Sink"]
        r_7 = ["Source", 11, 4, "Sink"]
        r_8 = ["Source", 3, 1, "Sink"]
        ini = [r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8]
        self.data.solve(initial_routes=ini, dive=True)
        assert int(self.data.best_value) == 450

    def test_subproblem_cspy_with_initial_routes(self):
        # benchmark result
        # http://vrp.galgos.inf.puc-rio.br/index.php/en/
        r_1 = ["Source", 2, "Sink"]
        r_2 = ["Source", 6, "Sink"]
        r_3 = ["Source", 8, "Sink"]
        r_4 = ["Source", 15, 12, 10, "Sink"]
        r_5 = ["Source", 14, 5, "Sink"]
        r_6 = ["Source", 13, 9, 7, "Sink"]
        r_7 = ["Source", 11, 4, "Sink"]
        r_8 = ["Source", 3, 1, "Sink"]
        ini = [r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8]
        self.data.solve(initial_routes=ini, cspy=True)
        assert int(self.data.best_value) == 450

    def test_subproblem_cspy_with_initial_routes_true(self):
        # benchmark result
        # http://vrp.galgos.inf.puc-rio.br/index.php/en/
        r_1 = ["Source", 2, "Sink"]
        r_2 = ["Source", 6, "Sink"]
        r_3 = ["Source", 8, "Sink"]
        r_4 = ["Source", 15, 12, 10, "Sink"]
        r_5 = ["Source", 14, 5, "Sink"]
        r_6 = ["Source", 13, 9, 7, "Sink"]
        r_7 = ["Source", 11, 4, "Sink"]
        r_8 = ["Source", 3, 1, "Sink"]
        ini = [r_1, r_2, r_3, r_4, r_5, r_6, r_7, r_8]
        self.data.solve(initial_routes=ini, cspy=True, dive=True)
        assert int(self.data.best_value) == 450
