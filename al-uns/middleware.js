/**
 * Pass-through middleware.
 * Host routing for al-munya.com is handled only by vercel.json rewrites/redirects.
 * Do NOT use Response.rewrite — it is not a valid Web API and crashes Edge.
 */
export default function middleware() {
  // intentional no-op
}
