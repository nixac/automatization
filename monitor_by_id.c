// gcc monitor_by_id.c -o monitor_by_id -lX11 -lXrandr
#include <X11/Xlib.h>
#include <X11/extensions/Xrandr.h>
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[])
{
    int vmajor = 0;
    int vminor = 0;
    int moni = -1;
    int monc = 0;
    if (argc == 2) moni = atoi(argv[1]);

    Display *dpy = XOpenDisplay(NULL);
    if (!dpy || moni < 0) return 1;
    Window wnd = XDefaultRootWindow(dpy);

    if (XRRQueryExtension(dpy, &vmajor, &vminor))
    {
        XRRQueryVersion(dpy, &vmajor, &vminor);
        XRRMonitorInfo *info = XRRGetMonitors(dpy, wnd, 0, &monc);
        if (moni >= monc) return 1;

        printf("%s\n", XGetAtomName(dpy, info[moni].name));

        XFree(info);
    }

    XCloseDisplay(dpy);
    return 0;
}