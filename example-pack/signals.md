# Signals: what to search for, and what it means (ServiceTitan)

Signal types: **catalyst** (makes the problem worse), **symptom** (shows they have it), **intent** (shows they are looking), **absence** (something that should be there and is not). An absence signal has no event date: label it "absence, checked [today's date]".

Replace `[company]`, `[city]`, and `[person]` with the real values.

## Tier 1: catalysts
| Signal | Type | What it looks like | Where to look | Freshness | Confidence |
|---|---|---|---|---|---|
| Bought by a PE platform, or bought an add on | catalyst | A platform buys them, or they buy a smaller shop | Trade press, the platform's own press page, their site | 180 days | high |
| New location or new metro | catalyst | A second or third branch opens | Their site, local news, job posts | 120 days | high |
| Hiring a wave of technicians | catalyst | Several open tech roles at once | Indeed, their careers page | 60 days | high |
| New GM, COO, CFO, or director of operations | catalyst | A first professional manager above the owner | LinkedIn, their site, local news | 120 days | high |
| Adding a trade | catalyst | A plumbing shop adds HVAC, or electrical | Their services pages, news | 180 days | medium |

## Tier 2: symptoms
| Signal | Type | What it looks like | Where to look | Freshness | Confidence |
|---|---|---|---|---|---|
| Reviews about no answer, no show, or a late tech | symptom | "Nobody ever called me back", "window was 8 to 12, came at 4" | Google and Yelp ratings and counts through the research route; review text where a page will load | 90 days | medium |
| Hiring a CSR, dispatcher, or office manager | symptom | The office is the bottleneck | Indeed, their careers page | 60 days | medium |
| Hiring an AR or billing clerk | symptom | Collections are manual | Indeed, their careers page | 60 days | medium |
| Seasonal overload language | symptom | "Due to high call volume", emergency banners | Their homepage | 60 days | low |

## Tier 3: intent and absence
| Signal | Type | What it looks like | Where to look | Freshness | Confidence |
|---|---|---|---|---|---|
| Running a direct competitor | intent | A booking or client portal on a competitor domain | Their book, schedule, or pay buttons | current | high |
| No online booking | absence | Phone number only, or a contact form that goes to email | Their site | checked today | high |
| No online payment | absence | "Mail your check", or no pay link at all | Their site | checked today | high |
| No membership or maintenance plan page | absence | Nothing recurring to sell | Their site | checked today | medium |
| Hiring on a job board with no careers page | absence | Growth the site has not caught up with | Indeed versus their site | checked today | medium |

## Search recipes
| Signal | Recipe |
|---|---|
| Acquisition | `"[company]" acquired OR acquisition OR "joins" OR "partners with"`; then `"[company]" [platform name] press release` |
| PE platform check | `"[company]" "Apex Service Partners" OR "Wrench Group" OR "Sila Services" OR "TurnPoint" OR "Comfort Systems"` |
| New location | `"[company]" "now serving" OR "new location" OR "second location" [city]` |
| Technician hiring | `"[company]" hiring technician site:indeed.com`; then their own /careers page |
| Office hiring | `"[company]" hiring CSR OR dispatcher OR "office manager" OR "accounts receivable"` |
| Leadership change | `"[company]" "[person]"`; and `"[company]" names OR appoints CEO OR president OR COO OR general manager` |
| Service complaints | Google reviews for [company] in [city]; look for no answer, no show, billing error, dated inside 90 days |
| Competitor platform | Open their book, schedule, request service, and pay buttons and read the domain each one lands on |
| Do they already run us | `site:myservicetitan.com "[company]"`; then `"[company]" ServiceTitan` for job posts and mentions, which are a CHECK FIRST and not a stop |

## One level deeper
Never stop at the headline.
| Signal | The deeper question |
|---|---|
| Acquisition | Who runs day to day now, and are the two companies on one system or two? Leadership is usually named after the deal, not with it. |
| New location | Does the second branch share dispatch with the first, or run its own board? |
| Technician hiring | How many trucks does that take them to, and can the office schedule that many? |
| New GM or COO | What were they brought in to fix, and what did they run before? |
| Service complaints | Do nearby competitors answer the phone better? That comparison is the pressure. |
| No online booking | Where does the site send a customer at 9pm, and who picks that call up in the morning? |

## Known vendor domains
Open the book, schedule, request service, portal, and pay buttons and read where each one lands.
| Domain | Vendor | What it means |
|---|---|---|
| `scheduler.servicetitan.com`, `static.servicetitan.com` | **ServiceTitan, us** | Already a customer. Stop, and say so with the link. (found live on leesair.com, 2026-09-22) |
| `<name>.myservicetitan.com` | **ServiceTitan, us** | Their own tenant login. Already a customer. Search `site:myservicetitan.com "[company]"` before you decide. (found live: berkeysmvp.myservicetitan.com, 2026-09-22) |
| `clienthub.getjobber.com` | Jobber | Competitor, and a size clue: Jobber skews small (found: https://clienthub.getjobber.com/booking/625ba5d1-f838-43d9-b9fa-63171fb8480a) |
| `book.housecallpro.com` | Housecall Pro | Competitor, skews small to mid (found: https://book.housecallpro.com/) |
| `scheduleengine.com` | Schedule Engine | Now part of ServiceTitan. Treat as a lead, not a customer, and check the rest of the site. (found: https://www.scheduleengine.com/service-titan) |
| fieldedge, servicefusion, workiz, successware, serviceautopilot, servicetrade in a URL | those vendors | Competitor signal. Domains unconfirmed: read the actual link before you claim it. |

## Signal to problem mapping
| Signal | What it means for them | Persona | Primary problem | Secondary |
|---|---|---|---|---|
| Bought by a platform, or bought an add on | Two companies, two systems, one set of numbers due to the board | Platform executive | post-deal-integration | slow-cash |
| New location or new metro | The office runs two boards at once | GM or operations | tech-productivity | missed-calls |
| Hiring a wave of technicians | More trucks than the office can schedule or measure | Owner | tech-productivity | missed-calls |
| New GM, COO, or CFO | Someone new is being measured on numbers nobody can see | GM or operations | tech-productivity | slow-cash |
| Hiring a CSR or dispatcher | Calls are being missed today | Office and CSR manager | missed-calls | tech-productivity |
| Hiring an AR or billing clerk | Cash is stuck in manual collections | Owner | slow-cash | post-deal-integration |
| Reviews about no answer or no show | Lost jobs are already public | Owner | missed-calls | tech-productivity |
| No online booking | Every call after hours goes to a competitor | Owner | missed-calls | |
| No online payment | Invoices wait on a check | Owner | slow-cash | |
| Running a direct competitor | They already buy software, so this is a switch, not a first purchase | any | whichever the competitor is weakest at | |

## Stacking
Two or more of these tell one story. Write it as one line.
- **The deal stack:** acquisition plus a new GM plus office hiring. A platform is being built and the back office is being rebuilt with it.
- **The growth stack:** technician hiring plus a new location plus complaints about no answer. They are selling more than they can deliver.
- **The cash stack:** no online payment plus an AR hire plus a membership page that does not exist. Money earned and not collected.
