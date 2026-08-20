export const config = {
  matcher: ['/', '/index.html'],
};

export default function middleware(request) {
  const host = request.headers.get('host') || '';
  if (host === 'al-munya.com' || host === 'www.al-munya.com') {
    const url = new URL(request.url);
    url.pathname = '/al-munya/index.html';
    return Response.rewrite(url);
  }
}
