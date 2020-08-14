from flask import Flask, jsonify, request

from src.hackerank_news_data_factory import HackerRankDataFactory as HackerRankDataFactory


from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)


@app.route('/hacker-news-top-10')
def hacker_news_top_10():
    return jsonify(HackerRankDataFactory().get_hackrank_news_top_10())

metrics = PrometheusMetrics(app)


metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/')
def main():
    pass

@app.route('/skip')
@metrics.do_not_track()
def skip():
    pass

@app.route('/<item_type>')
@metrics.do_not_track()
@metrics.counter('invocation_by_type', 'Number of invocations by type',
         labels={'item_type': lambda: request.view_args['type']})
def by_type(item_type):
    pass  

@app.route('/long-running')
@metrics.gauge('in_progress', 'Long running requests in progress')
def long_running():
    pass

@app.route('/status/<int:status>')
@metrics.do_not_track()
@metrics.summary('requests_by_status', 'Request latencies by status',
                 labels={'status': lambda r: r.status_code})
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path',
                   labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
def echo_status(status):
    return 'Status: %s' % status, status
if __name__ == '__main__':
    app.run()
