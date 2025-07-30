import React from "react";

type CellType = "empty" | "robot" | "trash" | "base";

interface Props {
    grid: CellType[][];
}

const getColor = (type: CellType) => {
    switch (type) {
        case "trash":
            return "bg-red-500";
        case "robot":
            return "bg-blue-500";
        case "base":
            return "bg-green-500";
        default:
            return "bg-gray-200";
    }
};

export const Grid: React.FC<Props> = ({ grid }) => {
    return (
        <div className="grid" style={{ gridTemplateColumns: `repeat(${grid[0].length}, 1fr)` }}>
            {grid.flat().map((cell, i) => (
                <div
                    key={i}
                    className={`w-6 h-6 ${getColor(cell)} border border-gray-400`}
                ></div>
            ))}
        </div>
    );
};
