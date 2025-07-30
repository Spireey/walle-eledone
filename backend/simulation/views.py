from functools import wraps

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .runner.runner import Runner

runner = None
has_started_flag = False


@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello World!"})


def has_started(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        global has_started_flag
        if not has_started_flag:
            return Response(
                {"error": "Simulation has not been started."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return view_func(request, *args, **kwargs)

    return wrapper


@api_view(['POST'])
def start_simulation(request):
    global runner, has_started_flag
    if runner is None:
        return Response(
            {"error": "Grid has not been created."},
            status=status.HTTP_400_BAD_REQUEST
        )
    has_started_flag = True
    return Response({"status": "started"})


@api_view(['POST'])
@has_started
def step_simulation(request):
    runner.step()
    return Response(runner.get_state())

@api_view(['POST'])
def reset_simulation(request):
    global runner, has_started_flag
    runner = None
    has_started_flag = False
    return Response({"status": "Simulation has been reset."})


@api_view(['POST'])
def create_grid(request):
    global runner, has_started_flag
    if has_started_flag:
        return Response({"error": "Simulation has already been started."})

    robot_count = int(request.GET.get("robots", 5))
    trash_count = int(request.GET.get("trash", 50))
    runner = Runner(robot_count, trash_count)
    return Response(runner.get_grid())

@api_view(['GET'])
def get_visibility(request):
    global runner
    if runner is None:
        return Response({"error": "Grid has not been created."})
    return Response(runner.get_visibility())
