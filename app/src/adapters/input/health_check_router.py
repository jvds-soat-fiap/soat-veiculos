from fastapi import APIRouter, status, Path
from datetime import datetime

router = APIRouter()

@router.get(path='/actuator', status_code=status.HTTP_201_CREATED)
async def health_check():
    return {'status': 'UP', 'date_time': datetime.now()}