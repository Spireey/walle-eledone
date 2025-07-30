import React, {useEffect, useRef, useState} from "react";
import axios from "axios";
import { Grid } from "./components/Grid";

type CellType = "empty" | "robot" | "trash";

function App() {
    const [grid, setGrid] = useState<CellType[][]>([]);
    const [robots, setRobots] = useState(3);
    const [trash, setTrash] = useState(10);
    const [hasStarted, setHasStarted] = useState(false);
    const intervalRef = useRef<NodeJS.Timeout | null>(null);

    const handleCreateGrid = async () => {
        const res = await axios.post(`http://localhost:8000/create_grid?robots=${robots}&trash=${trash}`);
        setGrid(res.data.grid)
        setHasStarted(false);
    };

    const handleStart = async () => {
        await axios.post("http://localhost:8000/start_simulation");
        setHasStarted(true);
    };

    const handleReset = async () => {
        await axios.post("http://localhost:8000/reset_simulation");
        setGrid([]);
        setHasStarted(false);
    };

    useEffect(() => {
        (async () => {
            await handleReset();
        })()
    }, []);

    useEffect(() => {
        if (hasStarted) {
            intervalRef.current = setInterval(async () => {
                try {
                    const res = await axios.post("http://localhost:8000/step_simulation");
                    setGrid(prevGrid => {
                        const newGrid = prevGrid.map(row => [...row]);
                        for (const empty of res.data.emptied) {
                            if (empty[1] === 0 && empty[0] === 0) continue;
                            newGrid[empty[1]][empty[0]] = "empty";
                        }
                        for (const robot of res.data.robots) {
                            if (robot.x === 0 && robot.y === 0) continue;
                            newGrid[robot.y][robot.x] = "robot";
                        }
                        for (const trash of res.data.memory) {
                            newGrid[trash[1]][trash[0]] = "trash";
                        }
                        return newGrid;
                    })
                } catch (error) {
                    console.error("Erreur pendant la simulation :", error);
                }
            }, 150);
        }
        return () => {
            if (intervalRef.current) clearInterval(intervalRef.current);
        };
    }, [hasStarted]);


        return (
        <div className="min-h-screen bg-gray-50 p-6 text-center">
            <div className="flex flex-col items-center space-y-4 mb-6">
                {grid.length === 0 && (
                    <div className="flex space-x-4">
                        <input
                            type="number"
                            value={robots}
                            onChange={(e) => setRobots(Number(e.target.value))}
                            className="border px-3 py-1 rounded"
                            placeholder="Robots"
                        />
                        <input
                            type="number"
                            value={trash}
                            onChange={(e) => setTrash(Number(e.target.value))}
                            className="border px-3 py-1 rounded"
                            placeholder="Déchets"
                        />
                        <button
                            onClick={handleCreateGrid}
                            className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded"
                        >
                            Créer la grille
                        </button>
                    </div>
                )}

                {grid.length > 0 && (
                    <div className="flex space-x-4">
                        {!hasStarted && (
                            <button
                                onClick={handleStart}
                                className="bg-green-500 hover:bg-green-600 text-white px-4 py-2 rounded"
                            >
                                Démarrer
                            </button>
                        )}
                        <button
                            onClick={handleReset}
                            className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded"
                        >
                            Réinitialiser
                        </button>
                    </div>
                )}
            </div>

            {grid.length > 0 && (
                <div className="flex justify-center">
                    <Grid grid={grid} />
                </div>
            )}
        </div>
    );
}

export default App;
