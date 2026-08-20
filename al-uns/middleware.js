import { next } from '@vercel/edge';

export const config = {
  matcher: [
    '/',
    '/index.html',
    '/contact',
    '/contact.html',
    '/demeure',
    '/demeure.html',
    '/an-nudama',
  ],
};

const MUNYA_HOSTS = new Set(['al-munya.com', 'www.al-munya.com']);

const PATH_MAP = {
  '/': '/al-munya/index.html',
  '/index.html': '/al-munya/index.html',
  '/contact': '/al-munya/contact.html',
  '/contact.html': '/al-munya/contact.html',
  '/demeure': '/al-munya/demeure.html',
  '/demeure.html': '/al-munya/demeure.html',
  '/an-nudama': '/al-munya/an-nudama.html',
};

export default function middleware(request) {
  const host = (request.headers.get('host') || '').split(':')[0].toLowerCase();
  if (!MUNYA_HOSTS.has(host)) {
    return next();
  }

  const { pathname } = new URL(request.url);
  const dest = PATH_MAP[pathname];
  if (!dest) {
    return next();
  }

  return next({
    rewrite: new URL(dest, request.url),
  });
}
