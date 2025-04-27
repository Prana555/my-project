def optimize_containers(container_data):
    """
    Simple optimization: sort containers based on priority.
    """
    containers = container_data.get("containers", [])
    containers.sort(key=lambda x: x["priority"])
    return {"move_plan": containers}
