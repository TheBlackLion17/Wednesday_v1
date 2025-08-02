import logging
from aiohttp import web as webserver

# Setup logging for web server
logger = logging.getLogger("aiohttp.server")

# Define routes
routes = webserver.RouteTableDef()

# List of known malicious scan paths
SUSPICIOUS_PATHS = [
    "/cgi-bin/luci",
    "/actuator",
    "/actuator/gateway",
    "/admin",
    "/wp-login.php",
]

# Middleware for error handling and threat filtering
@webserver.middleware
async def error_middleware(request, handler):
    # Block suspicious paths
    if any(request.path.startswith(p) for p in SUSPICIOUS_PATHS):
        logger.warning(f"Blocked suspicious path: {request.path} from {request.remote}")
        return webserver.json_response({"error": "Forbidden"}, status=403)
    
    try:
        response = await handler(request)
        if response.status == 404:
            logger.info(f"404 Not Found: {request.method} {request.path}")
            return webserver.json_response({"error": "Not Found"}, status=404)
        return response
    except webserver.HTTPException as ex:
        return webserver.json_response({"error": ex.reason}, status=ex.status)
    except Exception as e:
        logger.exception("Unhandled exception in web server")
        return webserver.json_response({"error": "Internal Server Error"}, status=500)

# aiohttp app creation
async def bot_run():
    _app = webserver.Application(
        client_max_size=30_000_000,
        middlewares=[error_middleware]
    )
    _app.add_routes(routes)
    return _app

# Root route
@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return webserver.json_response(
        "Goutham Josh KuttuBot Web Supported . . . !  This is a preview of WeB . . .! ! !"
    )
