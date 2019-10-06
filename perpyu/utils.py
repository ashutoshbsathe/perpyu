import sys 

def progress(curr, total, suffix='', bar_len=48):
    filled = int(round(bar_len * curr / float(total))) if curr != 0 else 1
    bar = '=' * (filled - 1) + '>' + '-' * (bar_len - filled)
    sys.stdout.write('\r[%s](%d/%d) .. %s' % (bar, curr, total, suffix))
    sys.stdout.flush()
    if curr == total:
        bar = bar_len * '='
        sys.stdout.write('\r[%s](%d/%d) .. %s .. Completed' % (bar, curr, total, suffix))
    return 
    