export interface Robot {
    x: number;
    y: number;
    hasTrash: boolean;
}

export interface Trash {
    x: number;
    y: number;
}

export interface Base {
    x: number;
    y: number;
}

export interface SimulationState {
    width: number;
    height: number;
    base: Base;
    robots: Robot[];
    trash: Trash[];
}